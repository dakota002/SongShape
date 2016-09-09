function pointSets = uniForm(a,b,m,n_1,n_2,n_3,res)
theta=(-pi:res:pi);
phi=(-pi/2:res:pi/2);
pointSets=[];
for i=1:length(theta)
    for j=1:length(phi)
        t1=(m*theta(i)/4);
        t2=(m*phi(j)/4);
        r1=((abs(cos(t1)/a).^n_2)+((abs(sin(t1)/b).^n_3))).^(-1/n_1);
        r2=((abs(cos(t2)/a).^n_2)+((abs(sin(t2)/b).^n_3))).^(-1/n_1);
        x=r1*cos(theta(i))*r2*cos(phi(j));
        y=r1*sin(theta(i))*r2*cos(phi(j));
        z=r2*sin(phi(j));
        pointSets=[pointSets; x y z];
    end
end
