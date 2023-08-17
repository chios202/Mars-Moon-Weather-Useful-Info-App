#include "Mars.h"
#include "CustomExepction.h"
#include <vector>
#include <boost/asio.hpp>
#include <iostream>
#include <algorithm>



void Options::ReadData(const std::string &path)
{
    out.open(path);
    while (std::getline(out, data))
    {
        std::cout << data << '\n';
    }
}



void Options::TCPClient(const std::string& option) const
{
    boost::asio::io_context io_context;
    boost::asio::ip::tcp::endpoint endpoint(boost::asio::ip::address::from_string(m_ip),m_port);
    boost::asio::ip::tcp::socket socket(io_context);
    socket.connect(endpoint);

    while (true)
    {
        boost::asio::write(socket,boost::asio::buffer(option));

        boost::array<char,128> buffer{};
        boost::system::error_code errorCode;

        std::size_t len = socket.read_some(boost::asio::buffer(buffer),errorCode);
        if (errorCode == boost::asio::error::eof)
        {
            break;
        }
        std::cout.write(buffer.data(), len);
    }
}


int outData()
{
    std::cout << "Enter 1 for displaying upComingMoonPhases, 2 for weekly Mars weather:" << '\n';

    int x{};
    std::cin >> x;
    if (x > 2)
        throw CustomExeption{"Invalid number option!"};
    return x;

}

const std::string& TCPClientOption(const std::string& option)
{
    std::vector<std::string> options{"1","2"};
    auto finder = std::find(options.cbegin(), options.cend(), option);
    if (finder == options.cend())
        throw CustomExeption("Invalid option!");
    return option;
}

int main(int argc, char* argv[])
{

    Options file{};

    try
    {
        int path{outData()};
        file.ReadData(argv[path]);
    }
    catch (const CustomExeption& exeption)
    {
        std::cerr << "You provided an invalid option (" << exeption.what() << ")" << '\n';
    }

    Options TCPClientStart{"192.168.1.3",1234};

    std::cout << "Enter 1 for real-time MoonLro and 2 for Mars distance from sun:" << '\n';
    std::string option{};
    std::cin >> option;

    try
    {
        const std::string finalOption{TCPClientOption(option)};
        TCPClientStart.TCPClient(finalOption);
    }
    catch (const CustomExeption& exeption)
    {
        std::cerr << "You provided an invalid option (" << exeption.what() << ")" << '\n';
    }


    return 0;
}