package com.amazonaws.hw1;
/*
 * Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *  http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */

import java.util.Collection;
import java.util.List;

import com.amazonaws.AmazonClientException;
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.regions.Region;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.ec2.AmazonEC2;
import com.amazonaws.services.ec2.AmazonEC2Client;
import com.amazonaws.services.ec2.model.DescribeInstancesRequest;
import com.amazonaws.services.ec2.model.DescribeInstancesResult;
import com.amazonaws.services.ec2.model.Instance;
import com.amazonaws.services.ec2.model.Reservation;
import com.amazonaws.services.ec2.model.RunInstancesRequest;
import com.amazonaws.services.ec2.model.RunInstancesResult;

/**
 * Welcome to your new AWS Java SDK based project!
 *
 * This class is meant as a starting point for your console-based application
 * that makes one or more calls to the AWS services supported by the Java SDK,
 * such as EC2, SimpleDB, and S3.
 *
 * In order to use the services in this sample, you need:
 *
 * - A valid Amazon Web Services account. You can register for AWS at:
 * https://aws-portal.amazon.com/gp/aws/developer/registration/index.html
 *
 * - Your account's Access Key ID and Secret Access Key:
 * http://aws.amazon.com/security-credentials
 *
 * - A subscription to Amazon EC2. You can sign up for EC2 at:
 * http://aws.amazon.com/ec2/
 *
 */

public class CreateEC2SamplePart1 {

	/*
	 * Before running the code: Fill in your AWS access credentials in the provided
	 * credentials file template, and be sure to move the file to the default
	 * location where the sample code will load the credentials from.
	 * https://console.aws.amazon.com/iam/home?#security_credential
	 *
	 * WARNING: To avoid accidental leakage of your credentials, DO NOT keep the
	 * credentials file in your source directory.
	 */

	public static void main(String[] args) {
		// ============================================================================================//
		// =============================== Submitting a Request
		// =======================================//
		// ============================================================================================//

		/*
		 * The ProfileCredentialsProvider will return your [default] credential profile
		 * by reading from the credentials file.
		 */
		AWSCredentials credentials = null;
		try {
			credentials = new BasicAWSCredentials("AKIAJVDOI3E6RVV53A5Q", "FpXGguSULr9DwFlHsR4wEIaOXDk/t1YzsvJ72CkC");
		} catch (Exception e) {
			throw new AmazonClientException("Cannot load the credentials from the credential profiles file. "
					+ "Please make sure that your credentials file is at the correct "
					+ "location, and is in valid format.", e);
		}

		// Create the AmazonEC2Client object so we can call various APIs.
		@SuppressWarnings("deprecation")
		AmazonEC2 ec2 = new AmazonEC2Client(credentials);
		Region usWest2 = Region.getRegion(Regions.US_WEST_2);
		ec2.setRegion(usWest2);

		// Create a key pair
		// Fill code Here

		// Initializes a Run Instance Request
		RunInstancesRequest runInstancesRequest = new RunInstancesRequest();

		// Setup the specifications of the launch. This includes the instance type (e.g.
		// t2.micro)
		// and the latest Amazon Linux AMI id available. Note, you should always use the
		// latest
		// Amazon Linux AMI id or another of your choosing.
		runInstancesRequest.withImageId("ami-7172b611").withInstanceType("t2.micro").withMinCount(1).withMaxCount(1)
				.withKeyName("sareen_keypair").withSecurityGroups("sareen_security_group");

		RunInstancesResult runInstancesResult = ec2.runInstances(runInstancesRequest);

		// do something here to get the results after the instance is created

		DescribeInstancesRequest request = new DescribeInstancesRequest();
		Collection<String> instanceIds = null;
		request.setInstanceIds(instanceIds);
		DescribeInstancesResult result = ec2.describeInstances(request);
		List<Reservation> reservations = result.getReservations();
		List<Instance> instances;
		for (Reservation res : reservations) {
			instances = res.getInstances();
			for (Instance ins : instances) {
				System.out.println("Instance ID:" + ins.getInstanceId() + "\t Public IP: " + ins.getPublicIpAddress()
						+ "\t Region: " + ins.getPlacement().getAvailabilityZone());

			}

		}
	}
}
