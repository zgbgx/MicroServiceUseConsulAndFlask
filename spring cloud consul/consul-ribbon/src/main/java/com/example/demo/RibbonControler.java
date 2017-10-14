package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class RibbonControler {
	@Autowired
	RibbonService ribbonService;

	@RequestMapping(value = "/ribbon")
	public String ribbon() {
		return ribbonService.ribbonService();
	}

	@RequestMapping(value = "/health")
	public String checkhealth() {
		return "success";
	}

}
