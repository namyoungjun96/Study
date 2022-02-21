package net.youngjun.spring4.chap02;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import net.youngjun.spring4.chap02.conf.Config;

public class MainJavaConfig {

	public static void main(String[] args) {
		AnnotationConfigApplicationContext ctx =
				new AnnotationConfigApplicationContext(Config.class);
		
		AuthenticationService authSvc =
				ctx.getBean("authenticationService", AuthenticationService.class);
		authSvc.authenticate("bkchoi", "1234");
		
		PasswordChangeService pwChgSvc =
				ctx.getBean(PasswordChangeService.class);
		pwChgSvc.changePassword("bkchoi", "1234", "5678");
		
		ctx.close();
	}
	
}
