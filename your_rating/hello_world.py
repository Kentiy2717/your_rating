from typing import Literal


def get_DlgCode(old_DlgCode: int, Pri: Literal[1, 0], Sec: Literal[1, 0]) -> int:
    '''FUNCTION get_DlgCode : INT
VAR_INPUT
    old_DlgCode: INT;
    Pri: INT; (* 0 или 1 *)
    Sec: INT; (* 0 или 1 *)
END_VAR

CASE old_DlgCode OF
    0:
        IF Pri = 1 THEN
            get_DlgCode := 1;
        ELSIF Sec = 1 THEN
            get_DlgCode := 2;
        ELSE
            get_DlgCode := 0;
        END_IF;
    
    1:
        IF Pri = 1 THEN
            get_DlgCode := 1;
        ELSIF Sec = 1 THEN
            get_DlgCode := 2;
        ELSE
            get_DlgCode := 0;
        END_IF;
    
    2:
        IF Sec = 1 THEN
            get_DlgCode := 2;
        ELSIF Pri = 1 THEN
            get_DlgCode := 1;
        ELSE
            get_DlgCode := 0;
        END_IF;
    
    ELSE
        get_DlgCode := 0;
END_CASE;
END_FUNCTION'''
    if old_DlgCode == 0:
        if Pri:
            DlgCode = Pri
        elif Sec:
            DlgCode = Sec * 2
        else:
            DlgCode = 0
    elif old_DlgCode == 1:
        if Pri:
            DlgCode = 1
        elif Sec:
            DlgCode = 2
        else:
            DlgCode = 0
    elif old_DlgCode == 2:
        if Sec:
            DlgCode = 2
        elif Pri:
            DlgCode = 1
        else:
            DlgCode = 0
    return DlgCode

variables = (
    ((1, 0), (1, 1), (0, 1)),
    ((1, 0), (1, 1), (1, 0)),
    ((0, 1), (1, 1), (0, 1)),
    ((0, 1), (1, 1), (1, 0)),
)

for vars_ in variables:
    print(f'\n{vars_}:')
    old_DlgCode = 0
    for Pri, Sec in vars_:
        DlgCode = get_DlgCode(old_DlgCode=old_DlgCode, Pri=Pri, Sec=Sec)
        print(f'old_DlgCode={old_DlgCode}, Pri={Pri}, Sec={Sec} -> DlgCode={DlgCode}')
        old_DlgCode = DlgCode

        