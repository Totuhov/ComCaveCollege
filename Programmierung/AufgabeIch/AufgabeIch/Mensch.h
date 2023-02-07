#pragma once
#include <iostream>

using namespace std;

 class Mensch
 {
	 string vorname;
	 string nachname;
	 int alter;

  public:
	  virtual string GetVorname();
	  virtual void SetVorname(string vorname);
	  virtual string GetNachName();
	  virtual void SetNachname(string nachname);
	  virtual int GetAlter();
	  virtual void SetAlter(int alter);
 };

