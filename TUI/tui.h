#ifndef TUI_H
#define TUI_H

#include "../DRIVERS/pair.h"

typedef struct{
    int width;
    int height;    
} SIZE;

pair TUISize(void);

#endif