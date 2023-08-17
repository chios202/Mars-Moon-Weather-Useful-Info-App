#ifndef MARS_H
#define MARS_H
#include "Planets.h"
#include <iostream>
#include <fstream>
#include <utility>


class Options: public Interface
{
public:

    Options() = default;

    Options(std::string&& ip, int port)
    : Interface{std::move(ip), port}
    {

    }


     void ReadData(const std::string& path) override;
     void TCPClient(const std::string& option) const override;

};
#endif MARS_H
