#pragma once
#include "CMensch.h"

class CMitarbeiter : public CMensch
{
    double Gehalt;
public:
    double GetGehalt();
    void SetGehalt(double geld);
};

