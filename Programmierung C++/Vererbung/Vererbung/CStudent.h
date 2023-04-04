#pragma once
#include "CMensch.h"

class CStudent : public CMensch
{
private:
    short Semester;
public:
    short GetSemester();
    void SetSemester(short semester);
};
