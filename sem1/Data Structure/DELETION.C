#include<stdio.h>
#include<conio.h>
void main()
{
int a[10],i,n,pos;
clrscr();
printf("Enter the size of the array");
scanf("%d",&n);
printf("Enter the array elements");
for(i=0;i<n;i++){
scanf("%d",&a[i]);}
printf("Enter the position from which element to be deleted");
scanf("%d",&pos);
for(i=pos-1;i<n;i++)
a[i]=a[i+1];
printf("the new array");
for(i=0;i<n-1;i++)
printf("\n%d",a[i]);
getch();
}
