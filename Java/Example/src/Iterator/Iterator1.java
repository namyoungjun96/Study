package Iterator;

import java.util.*;

public class Iterator1 {
	public static void main(String[] args) {
		List list=new ArrayList();
		
		list.add("1");
		list.add("2");
		list.add("3");
		list.add("4");
		list.add("5");
		list.add("6");
		
		Iterator <String> itr=list.iterator();
		
		while(itr.hasNext()) {
			String str=itr.next();
			System.out.println(str);
		}
	}
}
