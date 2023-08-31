class outer{

	
	
	void test()
	
	{
	
		System.out.println("outer class");
		
	}
	
	class inner{
	
		void print()
		
		{
		
			System.out.println("inner class");
			
		}
		
	}
	
	static class stat{
	
		
		
		static void display()
		
		{
		
			System.out.println("static method in static inner class");
		
		}
		
		
		void view()
		
		{
		
			System.out.println("non static method in static inner class");
			
		}
		
		
	}
	
}


class nest{

	public static void main(String ar[])
	
	{
	
		outer ot=new outer();
		
		ot.test();
		
		outer.inner in=ot.new inner();
		
		in.print();
		
		outer.stat.display();
		
		outer.stat st=new outer.stat();
		
		st.view();
		
	}
	
}
		
		
		
			

