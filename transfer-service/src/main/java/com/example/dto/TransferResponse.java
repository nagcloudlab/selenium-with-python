package com.example.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
public class TransferResponse {

    private String transactionId;
    private String fromAccountNumber;
    private String toAccountNumber;
    private double amount;
    private String status;
    private String message;
    private String timestamp;
    
}
