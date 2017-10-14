package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.cloud.netflix.zuul.EnableZuulProxy;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

//入口application类添加注解@EnableZuulProxy，开起zuul路由网关功能
@EnableZuulProxy
@EnableDiscoveryClient
@SpringBootApplication
@RestController
public class ConsulZuulApplication {

	public static void main(String[] args) {
		SpringApplication.run(ConsulZuulApplication.class, args);
	}

	@RequestMapping(value = "/health")
	public String checkhealth() {
		return "success";
	}
}
