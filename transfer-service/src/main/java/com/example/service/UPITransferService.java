package com.example.service;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.example.dto.TransferRequest;
import com.example.dto.TransferResponse;
import com.example.entity.Account;
import com.example.exception.AccountNotFoundException;
import com.example.exception.BalanceException;
import com.example.repository.AccountRepository;

@Service
public class UPITransferService implements TransferService {

    private AccountRepository accountRepository;

    public UPITransferService(AccountRepository accountRepository) {
        this.accountRepository = accountRepository;
    }

    /**
     * Transfers money from one account to another.
     *
     * @param transferRequest the transfer request containing details of the transfer
     * @return a TransferResponse object containing the details of the transfer
     */
    @Transactional
    @Override
    public TransferResponse transfer(TransferRequest transferRequest) {

        // Load 'from' account
        Account fromAccount = accountRepository.findById(transferRequest.getFromAccountNumber())
        .orElseThrow(() -> new AccountNotFoundException("Account not found for number: " + transferRequest.getFromAccountNumber()));
        // Load 'to' account
        var toAccount = accountRepository.findById(transferRequest.getToAccountNumber())
        .orElseThrow(() -> new AccountNotFoundException("Account not found for number: " + transferRequest.getToAccountNumber()));
        // Check if the 'from' account has sufficient balance
        if (fromAccount.getBalance() < transferRequest.getAmount()) {
            throw new BalanceException("Insufficient balance in account: " + transferRequest.getFromAccountNumber());
        }
        // Perform the transfer
        fromAccount.setBalance(fromAccount.getBalance() - transferRequest.getAmount());
        toAccount.setBalance(toAccount.getBalance() + transferRequest.getAmount());
        // Save the updated accounts
        accountRepository.save(fromAccount);
        accountRepository.save(toAccount);
        // Create and return the transfer response
        TransferResponse transferResponse = new TransferResponse();
        transferResponse.setTransactionId("trx123456789");
        transferResponse.setFromAccountNumber(transferRequest.getFromAccountNumber());
        transferResponse.setToAccountNumber(transferRequest.getToAccountNumber());
        transferResponse.setAmount(transferRequest.getAmount());
        transferResponse.setStatus("SUCCESS");
        transferResponse.setMessage("Transfer successful");
        return transferResponse;
        
    }

  
    
}
