package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class RibbonService {
	@Autowired
	RestTemplate restTemplate;

	public String ribbonService() {
		return restTemplate.getForObject("http://doResponse/doResponse", String.class);
	}
}
