import java.util.Scanner;
import java.io.*;
public class kalukator {

    public static final String reset="\u001B[37m";
    public static final String c_red="\u001B[31m";

    public static void main(String[]args){
     // kalkulator simpel
     String enterKey = System.getProperty("line.separator");
     //enter
     Scanner a1=new Scanner(System.in);
     System.out.print("masukkan angka pertama:  ");
     int angka1=a1.nextInt();
     Scanner a2=new Scanner(System.in);
     System.out.print("masukkan angka kedua:  ");
     int angka2=a2.nextInt();
     Scanner obj=new Scanner(System.in);
     System.out.println("masukkan simbol operasi[+,-,x,/]  ");
     String op=obj.nextLine();
     
        System.out.println(enterKey+enterKey+enterKey);
        if(op.equals("+")){
         int h1=angka1+angka2;
         System.out.println("hasil dari "+angka1+op+angka2+" adalah "+h1);}
         else if(op.equals("-")){
         int h1=angka1-angka2;
         System.out.println("hasil dari "+angka1+op+angka2+" adalah "+h1);}
        else if(op.equals("x")){
         int h1=angka1*angka2;
         System.out.println("hasil dari "+angka1+op+angka2+" adalah "+h1);}
        else if(op.equals("/")){
         int h1=angka1/angka2;
         System.out.println("hasil dari "+angka1+op+angka2+" adalah "+h1);
        }else{
            System.out.println(c_red+"operasi tidak diketahui!"+reset);
        }
        System.out.println(enterKey+enterKey+enterKey);
    }
}