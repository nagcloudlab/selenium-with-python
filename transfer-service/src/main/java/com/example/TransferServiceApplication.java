package com.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;


@SpringBootApplication
public class TransferServiceApplication {

	public static void main(String[] args) {
		SpringApplication.run(TransferServiceApplication.class, args);
	}

	// @Bean
	// public CommandLineRunner commandLineRunner(TransferService transferService) {
	// 	return args -> {
	// 		// Example usage of the TransferService
	// 		TransferRequest transferRequest = new TransferRequest();
	// 		transferRequest.setFromAccountNumber("ACC002");
	// 		transferRequest.setToAccountNumber("ACC001");
	// 		transferRequest.setAmount(400.0);
	// 		transferService.transfer(transferRequest);
	// 	};
	// }

}
