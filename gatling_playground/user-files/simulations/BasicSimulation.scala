package computerdatabase

import io.gatling.core.Predef._
import io.gatling.http.Predef._
import scala.concurrent.duration._

class BasicSimulation extends Simulation {

  val httpProtocol = http // 4
    .baseUrl("http://localhost:8080") // 5
    .doNotTrackHeader("1")
    .acceptLanguageHeader("en-US,en;q=0.5")
    .acceptEncodingHeader("gzip, deflate")
    .userAgentHeader(
      "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0"
    )

  val users = scenario("Users").exec(
    http(
      "Home"
    ) // let's give proper names, as they are displayed in the reports
      .get("/")
  )

  setUp(
    users.inject(rampUsers(10) during (10 seconds))
  ).protocols(httpProtocol)
}