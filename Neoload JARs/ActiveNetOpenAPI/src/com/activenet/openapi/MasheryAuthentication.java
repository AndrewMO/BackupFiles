package com.activenet.openapi;

import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.time.Instant;

public class MasheryAuthentication {

	private static String sha256Hash(String message) {
		MessageDigest md = null;
		try {
			md = MessageDigest.getInstance("SHA-256");
		} catch (NoSuchAlgorithmException e) {
			e.printStackTrace();
		}
		md.update(message.getBytes(StandardCharsets.UTF_8));
		byte[] hash = md.digest();
		StringBuffer hexString = new StringBuffer();
		for (int i = 0; i < hash.length; i++) {
			String hex = Integer.toHexString(0xff & hash[i]);
			if (hex.length() == 1)
				hexString.append('0');
			hexString.append(hex);
		}
		return hexString.toString();
	}

	private static String getTimestamp() {
		Instant instant = Instant.now();
		long timeStampMillis = instant.getEpochSecond();
		return String.valueOf(timeStampMillis);
	}

	public static String getAuthenticationToken(String apiKey,String sharedSecret) {
		String timestamp = getTimestamp();
		return sha256Hash(apiKey + sharedSecret + timestamp);
	}

	public static void main(String[] args) {
		String apiKey = "ehvbahctq9nubvtyp4vnk3dj";
		String sharedSecret = "sJab25rpSF";
		
		System.out.println(getAuthenticationToken(apiKey,sharedSecret));

	}

}
