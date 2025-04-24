package com.example.api;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.dto.TransferRequest;
import com.example.dto.TransferResponse;
import com.example.service.TransferService;

import jakarta.validation.Valid;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;


@RestController
@RequestMapping("/api/v1/transfer")
public class TransferApiController {

    private final TransferService transferService;
    public TransferApiController(TransferService transferService) {
        this.transferService = transferService;
    }

    @PostMapping(
        consumes = "application/json",
        produces = "application/json"
    )
    public TransferResponse transfer(@RequestBody @Valid TransferRequest transferRequest) {
        // Call the transfer service to perform the transfer
        TransferResponse response = transferService.transfer(transferRequest);
        // Return the result as a JSON response
        return response;
    }
    

    
}
