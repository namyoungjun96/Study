package net.youngjun.spring4.chap05;

import org.springframework.beans.BeansException;
import org.springframework.beans.FatalBeanException;
import org.springframework.beans.MutablePropertyValues;
import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.beans.factory.config.BeanFactoryPostProcessor;
import org.springframework.beans.factory.config.ConfigurableListableBeanFactory;

public class ThresholdRequiedBeanFactoryPostProcessor implements BeanFactoryPostProcessor {

	private int defaultThreshold;
	
	public void setDefaultThreshold(int defaultThreshold) {
		this.defaultThreshold = defaultThreshold;
	}
	
	@Override
	public void postProcessBeanFactory(ConfigurableListableBeanFactory beanFactory) throws BeansException {
		// TODO Auto-generated method stub
		String[] beanNames = beanFactory.getBeanDefinitionNames();
		for (String name : beanNames) {
			BeanDefinition beanDef = beanFactory.getBeanDefinition(name);
			Class<?> klass = getClassFromBeanDef(beanDef);
			if(klass != null && ThresholdRequired.class.isAssignableFrom(klass)) {
				MutablePropertyValues prop = beanDef.getPropertyValues();
				if(!prop.contains("threshold")) {
					prop.add("threshold", defaultThreshold);
				}
			}
		}
	}
	
	private Class<?> getClassFromBeanDef(BeanDefinition beanDef) {
		if(beanDef.getBeanClassName() == null) return null;
		try {
			return Class.forName(beanDef.getBeanClassName());
		} catch (ClassNotFoundException e) {
			throw new FatalBeanException(e.getMessage(), e);
		}
	}
	
}
