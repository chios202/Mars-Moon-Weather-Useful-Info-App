#ifndef CUSTOMEXEPCTION_H
#include <iostream>
#include <exception>

class CustomExeption: public std::exception
{
private:
    std::string m_error{};
public:


    CustomExeption(std::string error)
    : m_error{error}
    {

    }

    const char* what() const noexcept override
    {
        return m_error.c_str();
    }
};
#define CUSTOMEXEPCTION_H

#endif CUSTOMEXEPCTION_H
