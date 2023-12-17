package com.example.facebook;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    EditText email,pwd;
    Button login,signup;
    CheckBox save,terms;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        email=(EditText) findViewById(R.id.email);
        pwd=(EditText) findViewById(R.id.pwd);
        login=(Button) findViewById(R.id.login);
        signup=(Button) findViewById(R.id.signup);
        save=(CheckBox) findViewById(R.id.save);
        terms=(CheckBox) findViewById(R.id.terms);
    }
    public void nextPage(View view) {
        Toast.makeText(this,"Login Successful",Toast.LENGTH_LONG).show();
    }

    public void gotoSignup(View view) {
        Toast.makeText(this,"Signup Successful",Toast.LENGTH_LONG).show();
    }
}
