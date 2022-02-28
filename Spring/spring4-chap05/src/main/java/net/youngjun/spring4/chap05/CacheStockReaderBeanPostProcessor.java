package net.youngjun.spring4.chap05;

import org.springframework.beans.BeansException;
import org.springframework.core.Ordered;

public class CacheStockReaderBeanPostProcessor implements BeanPostProcessor, Ordered {
	
	private int order;
	
	@Override
	public int getOrder() {
		return order;
	}
	
	public void setOrder(int order) {
		this.order = order;
	}
	
	@Override
	public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
		return bean;
	}
	
	@Override
	public Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException {
		if (StockReader.class.isAssignableFrom(bean.getClass()))
			return new CacheStockReader((StockReader) bean);
		else
			return bean;
	}

}
