package main

import (
	"fmt"
	"log"
	"net/http"
	"time"

	bolt "go.etcd.io/bbolt"
)

var world = []byte("world")
var key = []byte("hello")

func storeInitData(db *bolt.DB) {
	// store some data
	value := []byte("Hello World!")

	err := db.Update(func(tx *bolt.Tx) error {
		bucket, err := tx.CreateBucketIfNotExists(world)
		if err != nil {
			return err
		}

		err = bucket.Put(key, value)
		if err != nil {
			return err
		}
		return nil
	})

	if err != nil {
		log.Fatal(err)
	}
}

func getOpenedDbConnection() *bolt.DB {
	db, err := bolt.Open("./bolt.db", 0644, &bolt.Options{Timeout: 1 * time.Second})
	if err != nil {
		log.Fatal(err)
	}
	return db
}

func setupServer() {
	db := getOpenedDbConnection()
	defer db.Close()

	storeInitData(db)

	http.HandleFunc("/", getDbContentHandler)
	http.ListenAndServe(":80", nil)
}

func getDbContentHandler(w http.ResponseWriter, r *http.Request) {
	db := getOpenedDbConnection()
	defer db.Close()

	// retrieve the data
	db.View(func(tx *bolt.Tx) error {
		bucket := tx.Bucket(world)
		if bucket == nil {
			return fmt.Errorf("Bucket %q not found!", world)
		}

		val := bucket.Get(key)
		fmt.Fprintf(w, "The key: %d contains value: %d", key, val)

		fmt.Println(string(val))
		return nil
	})
}

func main() {
	setupServer()
}
