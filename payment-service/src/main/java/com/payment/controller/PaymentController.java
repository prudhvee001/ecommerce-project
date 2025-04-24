package com.payment.controller;

import org.springframework.web.bind.annotation.*;

import java.util.Map;

@RestController
@RequestMapping("/payment")
public class PaymentController {

    @PostMapping("/pay")
    public String pay(@RequestBody Map<String, Object> paymentInfo) {
        return "Payment processed for user " + paymentInfo.get("user_id");
    }

    @GetMapping("/status")
    public String status() {
        return "Payment status: Success";
    }
}
