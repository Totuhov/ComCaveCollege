#pragma once
#include "CMensch.h"

class CDozent : public CMensch
{
    bool Lehrbefaehigung;
public:
    bool GetLehrbefaehigung();
    void SetLehrbefaehigung(bool lehr);
};


