package com.example.spinner;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ImageView;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity2 extends AppCompatActivity implements AdapterView.OnItemSelectedListener {
    int image[]={R.drawable.india, R.drawable.uk, R.drawable.austalia};
    Spinner sp;
    ImageView i;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        sp = (Spinner) findViewById(R.id.sp);
        sp.setOnItemSelectedListener(this);

    }

    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
        i = (ImageView) findViewById(R.id.img);
        i.setImageResource(image[position]);
        TextView myText = (TextView) view;
        Toast.makeText(this, "You selected: "+myText.getText(),Toast.LENGTH_SHORT).show();
    }

    @Override
    public void onNothingSelected(AdapterView<?> parent) {

    }
}
