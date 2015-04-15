import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class DbInputGen 
{
		private static int NAME = 0;
		private static int SIZE = 5;
		private static int BLKSIZE = 6;
		private static int THRDGRP = 7;
		private static int BANKS = 8;
		private static int LATENCY = 9;
		private static int L2NAME = 10;
		private static int L1NAME = 11;
		
		private static boolean TXTRDONE = false;
		
		private final static int BytesPerKB = 1024;
		private final static int BytesPerMB = BytesPerKB*BytesPerKB;
		private final static int BytesPerGB = BytesPerMB*BytesPerKB; 
		private final static int BytesPerTB = BytesPerGB*BytesPerKB;
		
		private static ArrayList<String> L2CahceDetails = new ArrayList<String>();
		private static ArrayList<String> L1CahceDetails = new ArrayList<String>(); 
		
		private static long convertSize(long sizeArg, char meas) {
			long size = sizeArg;
			switch(meas){
			case 'K': size = size*BytesPerKB; break;
			case 'M': size = size*BytesPerMB; break;
			case 'G': size = size*BytesPerGB; break;
			case 'T': size = size*BytesPerTB; break;
			}
			return size;
		}

		private static String getSize(String[] thisLine){
			long size=0, size1=0, size2=0;
			String output;
			boolean size1Pres = false, size2Pres = false;
				
			if(thisLine[SIZE].charAt(0)=='<')
			{
				size = Integer.parseInt(thisLine[SIZE].substring(1, thisLine[SIZE].length()-1));
				size1Pres = true;
				
				if(thisLine[SIZE+1].charAt(thisLine[SIZE+1].length()-1) == '>')
					size1 = Integer.parseInt(thisLine[SIZE+1].substring(0, thisLine[SIZE+1].length()-2));
				else
				{
					size1 = Integer.parseInt(thisLine[SIZE+1].substring(0, thisLine[SIZE+1].length()-1));
					size2 = Integer.parseInt(thisLine[SIZE+2].substring(0, thisLine[SIZE+2].length()-2));
					size2Pres = true;
				}
			}	
			else
				size = Integer.parseInt(thisLine[SIZE].substring(0, thisLine[SIZE].length()-1));

			size = convertSize(size,thisLine[SIZE].charAt(thisLine[SIZE].length()-1));
			output =  Long.toString(size);
			if(size1Pres)
			{
				if(!size2Pres)
				{
					size1 = convertSize(size1, thisLine[SIZE+1].charAt(thisLine[SIZE+1].length()-2));
					/* Concat 2nd part of the size */
					output = output.concat(" ");
					output = output.concat(Long.toString(size1));
				}
				else
				{
					size1 = convertSize(size1, thisLine[SIZE+1].charAt(thisLine[SIZE+1].length()-1));
					/* Concat 2nd part of the size */
				    output = output.concat(" ");
					output = output.concat(Long.toString(size1));
					size2 = convertSize(size2, thisLine[SIZE+2].charAt(thisLine[SIZE+2].length()-2));
					/* Concat 3rd part of the size */
					output = output.concat(" ");
					output = output.concat(Long.toString(size2));
				}
			}
			return output;
		}
	
		private static String getUpLevels(String[] input, String l2, String l1) {
			String out="";
			String[] thisLine=null;
			int i=0;
			int l1SizeIndex = 5,l2SizeIndex = 5, l1CacheLineSize = 6, l2CacheLineSize = 6, l1Latency = 9, l2Latency = 9;
			for(i=0;i<input.length;i++)
			{
				thisLine = input[i].replaceAll("(^\\s+|\\s+$)", "").split("\\s+");
				if(thisLine[NAME].equalsIgnoreCase(l2))
				{
					if(thisLine[l2CacheLineSize].charAt(0)=='<')
					{
						l2Latency++;
					}
					out = out.concat(getSize(thisLine));
					out = out.concat(" ");
					out = out.concat(thisLine[BLKSIZE].replaceAll("\\D+",""));
					out = out.concat(" ");
					out = out.concat(thisLine[l2Latency].substring(0, thisLine[l2Latency].length()-3));
					out = out.concat(" ");
				}
				if(thisLine[NAME].equalsIgnoreCase(l1))
				{
					if(thisLine[l1CacheLineSize].charAt(0)=='<')
					{
						l1Latency++;
					}
					out = out.concat(getSize(thisLine));
					out = out.concat(" ");
					out = out.concat(thisLine[BLKSIZE].replaceAll("\\D+",""));
					out = out.concat(" ");
					out = out.concat(thisLine[l1Latency].substring(0, thisLine[l1Latency].length()-3));
					out = out.concat(" ");
				}
			}
			//System.out.println("Latency = "+out);
			return out;
		}
		
		private static String getText1D2DSize(String[] thisLine, int textID) {
			long size=0,size1=0;
			String output;
			boolean size1Pres = false;
			
			if(textID==1)
			{
				size = Long.parseLong(thisLine[5].substring(0, thisLine[5].length()-2));
				size1Pres = false; 
			}
			else if(textID == 2)
			{
				size = Long.parseLong(thisLine[5].substring(1, thisLine[5].length()-2));
				size1 = Long.parseLong(thisLine[6].substring(0,thisLine[6].length()-3));
				size1Pres = true;
			}
			size = convertSize(size, thisLine[5].charAt(thisLine[5].length()-2));
			output =  Long.toString(size);
			if(size1Pres)
			{
				size1 = convertSize(size1, thisLine[6].charAt(thisLine[6].length()-3));
				/* Concat 2nd part of the size */
				output = output.concat(" ");
				output = output.concat(Long.toString(size1));
				//System.out.println(output);
			}
			//System.out.println("Texture Out = "+output);
			return output;
		}
		
		private static String getOtherTextDetails(String[] in, String id) {
			String out = "";
			String[] thisLine;
			boolean text1=false,text2=false;
			int i=0;
			
			for(i=0;i<in.length;i++)
			{
				thisLine = in[i].replaceAll("(^\\s+|\\s+$)", "").split("\\s+");
				if(thisLine[1].equalsIgnoreCase(id))
				{
					if(text1==false)
					{
						text1=true;
						continue;
					}
					else if(text2==false)
					{
						text2=true;
						out = out.concat(getText1D2DSize(thisLine,1));
						out = out.concat(" ");
						continue;
					}
					else
					{
						out = out.concat(getText1D2DSize(thisLine,2));
						out = out.concat(" ");
					}
				}
			}
			return out;
		}
		
		private static void fillL2L1CacheDetails(char memType, String L2, String L1) {
			String memTypeFull = "";
			String L2SearchStr = "";
			String L1SearchStr = "";
			boolean L2Found = false;
			boolean L1Found = false;
			int i = 0, j = 0;
			String[] thisLine=null;
			
			switch (memType) {
			case 'g': memTypeFull = "_global"; break;
			case 'c': memTypeFull = "_constant"; break;
			case 'r': memTypeFull = "_readonly"; break;
			case 't': memTypeFull = "_texture"; break;
			default:  memTypeFull = "_none"; break;
			}
	
			switch (L2) {
			case "cL2": L2SearchStr = "L2_constant:"; break;
			case "tL2": L2SearchStr = "L2_texture:"; break;
			case "L2":  L2SearchStr = "L2:";
			default:    break;
			}
			
			switch (L1) {
			case "cL1": L1SearchStr = "L1_constant:"; break;
			case "tL1": L1SearchStr = "L1_texture:"; break;
			case "L1":  L1SearchStr = "L1_global:";
			default:    break;
			}
			
			for(i=0;i<L2CahceDetails.size();i++)
			{
				thisLine = L2CahceDetails.get(i).replaceAll("(^\\s+|\\s+$)", "").split("\\s+");
				if(thisLine[0].equalsIgnoreCase(L2SearchStr))
				{
					L2Found = true;
					L2CahceDetails.set(i, L2CahceDetails.get(i).concat(" L2"+memTypeFull));
				}
			}
			
			if(!L2Found)
			{
				L2CahceDetails.add(L2SearchStr+" L2"+memTypeFull);
			}
			
			for(i=0;i<L1CahceDetails.size();i++)
			{
				thisLine = L1CahceDetails.get(i).replaceAll("(^\\s+|\\s+$)", "").split("\\s+");
				if(thisLine[0].equalsIgnoreCase(L1SearchStr))
				{
					L1Found = true;
					L1CahceDetails.set(i, L1CahceDetails.get(i).concat(" L1"+memTypeFull));
				}
			}
			
			if(!L1Found)
			{
				L1CahceDetails.add(L1SearchStr+" L1"+memTypeFull);
			}
		}
	
		private static String getL2L1CacheDetails() throws IOException {
			int i=0;
			String output = "";
			
			for(i=0;i<L2CahceDetails.size();i++)
			{
				output = output.concat("- "+L2CahceDetails.get(i)+"\n");
			}
			for(i=0;i<L1CahceDetails.size();i++)
			{
				output = output.concat("-- "+L1CahceDetails.get(i)+"\n");
			}
			return output;
		}

		private static void parseWriteToFile(String[] in) throws IOException {
			String[] thisLine = null;
			String output = "";
			String l2Name = "";
			String l1Name = "";
			int i=0;
			long  size = 0;
			char sizeFirst;
			char blckSizeFirst;
			char thrdgrpFirst;
			char latencyFirst;
			File outFile = new File("configure.txt");	
			
			if(!outFile.exists())
				outFile.createNewFile();
			
			FileOutputStream fop = new FileOutputStream(outFile);
			
			for(i=0;i<in.length;i++)
			{
				thisLine = in[i].replaceAll("(^\\s+|\\s+$)", "").split("\\s+");
				sizeFirst = thisLine[SIZE].charAt(0);
				if(sizeFirst == '<')
				{
					BANKS++;
					LATENCY++;
					THRDGRP++;
					L2NAME++;
					L1NAME++;
					BLKSIZE++;
					
					/* If the size has three elements, increment the further things by 1 more */
					if(thisLine[SIZE+1].charAt(thisLine[SIZE+1].length()-1) != '>')
					{
						BANKS++;
						LATENCY++;
						THRDGRP++;
						L2NAME++;
						L1NAME++;
						BLKSIZE++;
					}
				}
				
				blckSizeFirst = thisLine[BLKSIZE].charAt(0);
				if(blckSizeFirst == '<')
				{
					THRDGRP++;
					BANKS++;
					LATENCY++;
					L2NAME++;
					L1NAME++;
					if(thisLine[BLKSIZE+1].charAt(thisLine[BLKSIZE+1].length()-1) != '>')
					{
						THRDGRP++;
						BANKS++;
						LATENCY++;
						L2NAME++;
						L1NAME++;
					}
				}
				
				thrdgrpFirst = thisLine[THRDGRP].charAt(0);
				if(thrdgrpFirst =='<')
				{
					BANKS++;
					LATENCY++;
					L2NAME++;
					L1NAME++;
				}
				
				latencyFirst = thisLine[LATENCY].charAt(0);
				if(latencyFirst == '<')
				{
					L1NAME++;
					L2NAME++;
				}
				
				switch(thisLine[NAME]){
				
					case "globalMem":
						output = output.concat("global ");
						output = output.concat(getSize(thisLine));
						output = output.concat(" ");
						output = output.concat(thisLine[LATENCY].split("[a-z]")[0]);
						output = output.concat(" ");
						if(thisLine[L2NAME].charAt(1)!='>')
						{
							output = output.concat(getUpLevels(in, thisLine[L2NAME].substring(1),thisLine[L1NAME].substring(0, thisLine[L1NAME].length()-1)));
							fillL2L1CacheDetails('g',thisLine[L2NAME].substring(1),thisLine[L1NAME].substring(0, thisLine[L1NAME].length()-1));
						}
						output = output.concat("\n");
						break;
						
					case "constantMem":
						output = output.concat("constant ");
						output = output.concat(getSize(thisLine));
						output = output.concat(" ");
						output = output.concat(thisLine[LATENCY].split("[a-z]")[0]);
						output = output.concat(" ");
						if(thisLine[L2NAME].charAt(1)!='>')
						{
							output = output.concat(getUpLevels(in, thisLine[L2NAME].substring(1),thisLine[L1NAME].substring(0, thisLine[L1NAME].length()-1)));
							fillL2L1CacheDetails('c',thisLine[L2NAME].substring(1),thisLine[L1NAME].substring(0, thisLine[L1NAME].length()-1));
						}
						output = output.concat("\n");
						break;
						
					case "readonlyMem":
						output = output.concat("constant ");
						output = output.concat(getSize(thisLine));
						output = output.concat(" ");
						output = output.concat(thisLine[LATENCY].split("[a-z]")[0]);
						output = output.concat(" ");
						if(thisLine[L2NAME].charAt(1)!='>')
						{
							output = output.concat(getUpLevels(in, thisLine[L2NAME].substring(1),thisLine[L1NAME].substring(0, thisLine[L1NAME].length()-1)));
							fillL2L1CacheDetails('r',thisLine[L2NAME].substring(1),thisLine[L1NAME].substring(0, thisLine[L1NAME].length()-1));
						}
						output = output.concat("\n");
						break;
						
					case "sharedMem":
						output = output.concat("shared ");
						output = output.concat(getSize(thisLine));
						output = output.concat(" ");
						output = output.concat(thisLine[BANKS]);
						output = output.concat(" ");
						output = output.concat(thisLine[LATENCY].split("[a-z]")[0]);
						output = output.concat(" ");
						if(thisLine[L2NAME].charAt(1)!='>')
						{
							output = output.concat(getUpLevels(in, thisLine[L2NAME].substring(1),thisLine[L1NAME].substring(0, thisLine[L1NAME].length()-1)));
							fillL2L1CacheDetails('s',thisLine[L2NAME].substring(1),thisLine[L1NAME].substring(0, thisLine[L1NAME].length()-1));
						}
						output = output.concat("\n");
						break;
					case "textureMem":
						if(!TXTRDONE){
							output = output.concat("texture ");
							output = output.concat(getOtherTextDetails(in,thisLine[1]));
							output = output.concat(thisLine[LATENCY].split("[a-z]")[0]);
							output = output.concat(" ");
							if(thisLine[L2NAME].charAt(1)!='>')
							{
								output = output.concat(getUpLevels(in, thisLine[L2NAME].substring(1),thisLine[L1NAME].substring(0, thisLine[L1NAME].length()-1)));
								fillL2L1CacheDetails('t',thisLine[L2NAME].substring(1),thisLine[L1NAME].substring(0, thisLine[L1NAME].length()-1));
							}
							output = output.concat("\n");

							TXTRDONE=true;
						}
						break;
				}
				
				THRDGRP = 7;
				BANKS = 8;
				LATENCY = 9;
				L2NAME = 10;
				L1NAME = 11; 
			}
			
			output = output.concat(getL2L1CacheDetails());
			fop.write(output.substring(0, output.length()-1).getBytes());
			fop.flush();
			fop.close();
			
			System.out.println("Input Generation Completed!!");
		}

		public static void main(String[] args) throws IOException {
			String file_input = new Scanner(new File("input.txt")).useDelimiter("\\A").next();
			String[] input = file_input.split("\n");
			
			parseWriteToFile(input);
		}
}
