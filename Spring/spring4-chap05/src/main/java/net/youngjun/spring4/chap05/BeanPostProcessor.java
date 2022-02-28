package net.youngjun.spring4.chap05;

import org.springframework.beans.BeansException;

public interface BeanPostProcessor {
	
	Object postProcessBeforeInitialization(Object bean, String beanName)
	throws BeansException;
	
	Object postProcessAfterInitialization(Object bean, String beanName)
	throws BeansException;

}
