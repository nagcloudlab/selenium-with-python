package com.example;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;

import io.restassured.builder.RequestSpecBuilder;
import io.restassured.builder.ResponseSpecBuilder;
import io.restassured.filter.log.LogDetail;
import io.restassured.specification.RequestSpecification;
import io.restassured.specification.ResponseSpecification;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;

import static io.restassured.RestAssured.given;

public class TransferApiTest {

    @Test
    public void beTrue() {
        // Arrange
        // Act
        // Assert
        assertThat(true, is(true));
       
    }

    protected static RequestSpecification transferRequestSpec;
    protected static ResponseSpecification transferResponseSpec;

    @BeforeEach
    public void setUp() {
        transferRequestSpec = new RequestSpecBuilder()
                .setBaseUri("http://localhost:8080")
                .setBasePath("/api/v1/transfer")
                .addHeader("Content-Type", "application/json")
                .log(LogDetail.ALL)
                .build();

         transferResponseSpec = new ResponseSpecBuilder()
                // .expectStatusCode(200)
                .expectContentType("application/json")
                .log(LogDetail.ALL)
                .build();
    }


    @Test
    public void testTransfer() {

        String requestBody = """
            {
              "fromAccountNumber": "ACC002",
              "toAccountNumber": "ACC001",
              "amount": 100.0
            }
            """;
       
        given()
                .spec(transferRequestSpec)
                .body(requestBody)
                .when()
                .post()
                .then()
                .spec(transferResponseSpec)
                .statusCode(200)
                .body("status", equalTo("SUCCESS"))
                .body("amount", equalTo(100.0f)) // for float/double use f
                .body("fromAccountNumber", startsWith("ACC002"))
                .body("toAccountNumber", startsWith("ACC001"))
                .body("transactionId", notNullValue());

    }
    
}
