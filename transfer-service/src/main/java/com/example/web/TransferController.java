package com.example.web;

import com.example.service.TransferService;
import com.example.dto.TransferRequest;
import com.example.dto.TransferResponse;
import com.example.exception.AccountNotFoundException;
import com.example.exception.BalanceException;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;


// View ( HTML ) Controller for handling transfer requests
@Controller
public class TransferController {

    private final TransferService transferService;

    public TransferController(TransferService transferService) {
        this.transferService = transferService;
    }

    // GET /transfer
    @RequestMapping(
            value = "/transfer",
            method = RequestMethod.GET
    )
    public String getTransferPage() {
        // Logic to display the transfer page
        return "transfer-form"; // View name for the transfer form
    }

    // POST /transfer
    @RequestMapping(
            value = "/transfer",
            method = RequestMethod.POST
    )
    public String handleTransfer(
           @ModelAttribute TransferRequest transferRequest,
           Model model
    ) {
        TransferResponse transferResponse=transferService.transfer(transferRequest);
        model.addAttribute("transferResponse", transferResponse);
        return "transfer-response"; // View name for the response page
    }

    @ExceptionHandler(
            { AccountNotFoundException.class, BalanceException.class }
    )
    public String handleTransferError(
            Exception exception,
            Model model
    ) {
        model.addAttribute("errorMessage", exception.getMessage());
        return "transfer-error"; // View name for the error page
    }

}