package com.cloud.chatbot;

import org.apache.log4j.Level;
import org.apache.log4j.LogManager;
import org.apache.log4j.Logger;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;


public class chatBotRequestHandler implements RequestHandler<Object, String> {
	
	final static Logger logger = Logger.getLogger(chatBotRequestHandler.class);

    @Override
    public String handleRequest(Object requestBody, Context context) {
    	LogManager.getRootLogger().setLevel(Level.INFO);
    	String request = requestBody.toString().toLowerCase();
    	
    	logger.info("JSON Request got is "+requestBody);
    	if(request.contains("hey")||request.contains("hi")||request.contains("hello")) {
    		return "Hello! How are you?";
    	}else if(request.contains("bye")){
    		return "Bye Bye!";
    	}else if(request.contains("namaste")){
    		return "Namaste Kaise ho app?";
    	}else {
    		return "Please try again";
    	}

        
    }
    
    
   

}
