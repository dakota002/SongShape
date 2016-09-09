%Makes points based on song using uniForm function
function out = songShape(Song,Resolution)
y = audioread(Song);
n=floor(length(y)/6);
y1=y(1:n);
y2=y(n+1:2*n);
y3=y(2*n+1:3*n);
y4=y(3*n+1:4*n);
y5=y(4*n+1:5*n);
y6=y(5*n+1:6*n);
Y=[y1;y2;y3;y4;y5;y6];
YT=Y.';
Z=(Y*YT)*1/(n);
e=eig(Z)*(2^8);
for i=1:length(e)
    if e(i)==0
        e(i)=1;
    end
end
diary songShape.txt
out=uniForm(e(1),e(2),e(3),e(4),e(5),e(6),Resolution)
diary off
