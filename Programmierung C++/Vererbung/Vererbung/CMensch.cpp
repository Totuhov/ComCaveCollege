#include "CMensch.h"

void CMensch::SetVorname(string SVorname)
{
    // TODO: F�gen Sie hier Ihren Implementierungscode ein..
    Vorname = SVorname;
}

void CMensch::SetNachname(string SNachname)
{
    // TODO: F�gen Sie hier Ihren Implementierungscode ein..
    Nachname = SNachname;
}

void CMensch::SetAlter(short SAlter)
{
    // TODO: F�gen Sie hier Ihren Implementierungscode ein..

    Alter = SAlter;
}

string CMensch::GetVorname()
{
    // TODO: F�gen Sie hier Ihren Implementierungscode ein..
    return Vorname;
}

string CMensch::GetNachname()
{
    // TODO: F�gen Sie hier Ihren Implementierungscode ein..
    return Nachname;
}

short CMensch::GetAlter()
{
    // TODO: F�gen Sie hier Ihren Implementierungscode ein..
    return Alter;
}
