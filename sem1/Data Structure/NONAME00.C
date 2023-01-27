#include<stdio.h>
#include<conio.h>
void main()
{
int a[10],i,n,pos,val;
clrscr();
printf("Enter the size of the array");
scanf("%d",&n);
printf("Enter the array elements");
for(i=0;i<n;i++){
scanf("%d",&a[i]);}
printf("Enter the position to which element to be inserted");
scanf("%d",&pos);
printf("Enter the element inserted to %d position",pos);
scanf("%d",&val);
i=n-1;
while(i>=pos-1){
a[i+1]=a[i];
i--;
}
a[pos-1]=val;
printf("New array");
for(i=0;i<=n;i++)
printf("%d\t",a[i]);
getch();
}
