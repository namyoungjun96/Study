package codingtest.company;

import java.io.*;
import java.util.*;
import java.util.Map.Entry;

public class Filehandler {
	private API[] api;
	private Web[] web;
	private HashMap<String, Integer> apiKeys;
	private Entry<String, Integer> maxEntry = null;
	private int browserCount = 0;

	// API�� WEB�� ������ ���� ��ü ����
	public Filehandler() {
		api = new API[] {
				new API("blog", 0),
				new API("book", 0),
				new API("image", 0),
				new API("knowledge", 0),
				new API("news", 0),
				new API("vclip", 0)
		};
		web = new Web[] {
				new Web("IE", 0),
				new Web("Chrome", 0),
				new Web("Safari", 0),
				new Web("Firefox", 0),
				new Web("Opera", 0)
		};
		apiKeys = new HashMap<String, Integer>();
	}

	// �α������� ������ �д� �޼���
	void Input(File path) {
		String temp = "";
		BufferedReader input = null;
		FileReader readFile = null;
		String[] apiHandler = {"blog", "book", "image", "knowledge", "news", "vclip"};
		String[] webHandler = {"IE", "Chrome", "Safari", "Firefox", "Opera"};
		try{
			readFile = new FileReader(path);
			input = new BufferedReader(readFile);
			String data = "";
			while((data = input.readLine()) != null) {
				String[] status = data.split("]");

				if(status[0].equals("[200")) {
					temp = status[1].substring(33);
					String[] apitemp = temp.split("\\?");
					apitemp[1] = apitemp[1].replaceAll("apikey=", "");
					apitemp[1] = apitemp[1].replaceAll("&q=dktechin", "");

					for(int i=0; i<apiHandler.length; i++) {
						if(apitemp[0].equals(apiHandler[i])) {
							api[i].plusCount();
						}
					}

					if(!apiKeys.containsKey(apitemp[1]))
						apiKeys.put(apitemp[1], 1);
					else
						apiKeys.put(apitemp[1], apiKeys.get(apitemp[1]) + 1);

					temp = status[2].substring(1);
					
					for(int i=0; i<webHandler.length; i++) {
						if(temp.equals(webHandler[i])) {
							web[i].plusCount();
							browserCount ++;
						}
					}
				}
			}
		} catch (IOException e) {
			System.out.println(e);
		} finally {
			try{
				readFile.close();
				input.close();
			} catch(IOException io) {}
		}
		
		Arrays.sort(api, new Comparator<API>() {
			@Override
			public int compare(API o1, API o2) {
				// TODO Auto-generated method stub
				return Integer.compare(o1.getCount(), o2.getCount());
			}
		});
		
		Set<Entry<String, Integer>> entrySet = apiKeys.entrySet();
		for (Entry<String, Integer> entry : entrySet) {
			if (maxEntry == null || entry.getValue() > maxEntry.getValue()) {
				maxEntry = entry;
			}
		}
	}

	// �ƿ�ǲ �α������� ����� �޼���
	void Output(String log) {
		try{
			File file = new File(log) ;
			
			if(!file.exists())
				file.createNewFile();
			
			FileWriter fw = new FileWriter(file) ;
			PrintWriter writer = new PrintWriter(fw);
			writer.println("�ִ�ȣ�� APIKEY");
			writer.println(maxEntry.getKey());
			writer.println("\n���� 3���� API ServiceID�� ������ ��û ��");
			for(int i=5; i>2; i--)
				writer.println(api[i].toString());
			writer.println("\n���������� ��� ����");
			for(int i=0; i<web.length; i++)
				writer.println(web[i].getName() + " : " + (int)((double)web[i].getCount() / (double)browserCount * 100) + "%");
			
			writer.close();
		} catch(Exception e){ e.printStackTrace(); }
	}
}
