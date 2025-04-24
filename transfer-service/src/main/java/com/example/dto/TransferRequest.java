package com.example.dto;

import io.swagger.v3.oas.annotations.media.Schema;
import jakarta.validation.constraints.DecimalMin;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Setter
@Getter
@AllArgsConstructor
@NoArgsConstructor
@Schema(description = "Request to transfer money between accounts")
public class TransferRequest {

    @Schema(description = "Account number from which amount is debited", example = "123456")
    @NotBlank(message = "From account must not be blank")
    private String fromAccountNumber;

    @Schema(description = "Account number to which amount is credited", example = "654321")
    @NotBlank(message = "To account must not be blank")
    private String toAccountNumber;

    @Schema(description = "Amount to transfer", example = "250.75")
    @NotNull(message = "Amount is required")
    @DecimalMin(value = "1", inclusive = true, message = "Amount must be greater than 0")
    private Double amount;

    
}