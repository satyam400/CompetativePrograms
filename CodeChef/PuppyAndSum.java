package st_h;


import java.util.Scanner;
class PuppyAndSum{
    void sum(int d,int n){
        int m=0;
        for(int j=d;j>=1;j--){
            m=0;
            for(int i=1;i<=n;i++){
                m=m+i;

            }
            n=m;
        }

        System.out.println(m);
    }
    public static void main(String[] args) {
        PuppyAndSum obj=new PuppyAndSum();
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        for(int i=0;i<t;i++){
            obj.sum(sc.nextInt(),sc.nextInt());
        }

    }
}
