#include "CMensch.h"

void CMensch::SetVorname(string SVorname)
{
    // TODO: Fügen Sie hier Ihren Implementierungscode ein..
    Vorname = SVorname;
}

void CMensch::SetNachname(string SNachname)
{
    // TODO: Fügen Sie hier Ihren Implementierungscode ein..
    Nachname = SNachname;
}

void CMensch::SetAlter(short SAlter)
{
    // TODO: Fügen Sie hier Ihren Implementierungscode ein..

    Alter = SAlter;
}

string CMensch::GetVorname()
{
    // TODO: Fügen Sie hier Ihren Implementierungscode ein..
    return Vorname;
}

string CMensch::GetNachname()
{
    // TODO: Fügen Sie hier Ihren Implementierungscode ein..
    return Nachname;
}

short CMensch::GetAlter()
{
    // TODO: Fügen Sie hier Ihren Implementierungscode ein..
    return Alter;
}
