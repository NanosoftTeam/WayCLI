project(WayCLI)
cmake_minimum_required(VERSION 3.0)

include_directories(include)

add_executable(WayCLI
  DRIVERS/pair.h
  TUI/tui.c
  TUI/tui.h
  main.c
  main.h
)