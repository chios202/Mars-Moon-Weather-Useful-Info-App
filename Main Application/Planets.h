#ifndef PLANETS_H
#define PLANETS_H
#include <iostream>
#include <fstream>
#include <boost/array.hpp>
#include <boost/asio.hpp>
#include <utility>

class Interface
{

protected:

    std::ifstream out{};
    std::string data{};

    std::string m_ip{};
    int m_port{};

protected:

    Interface() = default;

    Interface(std::string&& ip, int port)
    : m_ip{std::move(ip)}, m_port{port}
    {

    }

public:

    virtual void ReadData(const std::string& path) = 0;
    virtual void TCPClient(const std::string& option) const = 0;


};
#endif PLANETS_H
