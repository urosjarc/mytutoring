SET "DOT=C:\Program Files\dotnet"
SET "CITO=%cd%\cito\bin\Debug\net6.0"
set "PATH=%DOT%;%CITO%;%PATH%"

choco install dotnet -y

git clone https://github.com/pfusik/cito
cd cito
dotnet build
cd ..

cito
