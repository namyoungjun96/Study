package codingtest.company;

import java.io.File;

public class Main {
	public static void main(String[] args) {
		File path = new File("./src/source/input.log");
		Filehandler fileHandler = new Filehandler();
		fileHandler.Input(path);
		fileHandler.Output("./src/source/output.log");
	}
}