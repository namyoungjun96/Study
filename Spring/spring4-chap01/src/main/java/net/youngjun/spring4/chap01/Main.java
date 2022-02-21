package net.youngjun.spring4.chap01;

import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MavenBuildRunner buildRunner = new MavenBuildRunner();
		buildRunner.setMavenPath("C:\\apache-maven-3.8.4");
		
		Project sampleProject = new Project();
		List<String> srcDirs = new ArrayList<>();
		srcDirs.add("src");
		srcDirs.add("srcResources");
		sampleProject.setSrcDirs(srcDirs);
		sampleProject.setBinDir("bin");
		sampleProject.setBuildRunner(buildRunner);
		
		sampleProject.build();

	}

}
