#include <iostream>

class HelloWorld{
    public:
        void example_world(){
            std::cout << "hello world" << std::endl;
        }
};

// name mangling, make sure we can call this from Python
extern "C" {
    HelloWorld* HelloWorld_new(){ return new HelloWorld(); }
    void HelloWorld_example_world(HelloWorld* world){ world->example_world(); }
}
