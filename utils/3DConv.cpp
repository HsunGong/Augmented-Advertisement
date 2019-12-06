#include<bits/stdc++.h>
#define N 4100
#define M 4100
#define W 2666666
#define PB push_back
#define MP make_pair
#define X first
#define Y second
using namespace std;
using D=double;
const D eps=1e-8;
const double pi=acos(-1);
int sgn(D x){return x<-eps?-1:x>eps;}
int cmp(D x,D y){return sgn(x-y);}
int to[N][M],sz[N][M];
struct P{
	D x,y;
	P()=default;
	P(D x,D y):x(x),y(y){}
	P(const P&a):x(a.x),y(a.y){}
	P& operator=(const P&a){
		if(this==&a)return *this;
		x=a.x;y=a.y;
		return *this;
	}
	D norm(){return sqrt(x*x+y*y);}
	D norm2(){return x*x+y*y;}
	P unit(){
		D l=norm();
		return P(x/l,y/l);
	}
	P rot90(){return P(-y,x);}
	P _rot90(){return P(y,-x);}
	P rotate(D t){//弧度
		D c=cos(t),s=sin(t);
		return P(x*c-y*s,x*s+y*c);
	}
	D angle(){return atan2(y,x);}
};
bool operator==(const P&a,const P&b){return !cmp(a.x,b.x)&&!cmp(a.y,b.y);}
bool operator!=(const P&a,const P&b){return !(a==b);}
bool operator<(const P&a,const P&b){return cmp(a.x,b.x)==0?cmp(a.y,b.y)<0:cmp(a.x,b.x)<0;}
bool operator>(const P&a,const P&b){return cmp(a.x,b.x)==0?cmp(a.y,b.y)>0:cmp(a.x,b.x)>0;}
bool operator<=(const P&a,const P&b){return !(a>b);}
bool operator>=(const P&a,const P&b){return !(a<b);}
P operator-(const P&a){return P(-a.x,-a.y);}
P operator+(const P&a,const P&b){return P(a.x+b.x,a.y+b.y);}
P operator-(const P&a,const P&b){return P(a.x-b.x,a.y-b.y);}
P operator*(const P&a,D b){return P(a.x*b,a.y*b);}
P operator/(const P&a,D b){return P(a.x/b,a.y/b);}
D operator*(const P&a,const P&b){return a.x*b.x+a.y*b.y;}
D operator^(const P&a,const P&b){return a.x*b.y-a.y*b.x;}
D dot(const P&a,const P&b){return a.x*b.x+a.y*b.y;}
D det(const P&a,const P&b){return a.x*b.y-a.y*b.x;}
D dis(const P&a,const P&b){return (a-b).norm();}
D Area(const P&a,const P&b,const P&c){return fabs(det(b-a,c-a)*.5);}
D Area2(const P&a,const P&b,const P&c){return fabs(det(b-a,c-a));}
bool LeftTest(const P&a,const P&b,const P&s){return sgn(det(b-a,s-a))>0;}
bool RightTest(const P&a,const P&b,const P&s){return sgn(det(b-a,s-a))<0;}
bool FrontTest(const P&a,const P&b,const P&s){return sgn((b-a)*(s-a))>0;}
bool BehindTest(const P&a,const P&b,const P&s){return sgn((b-a)*(s-a))<0;}
			struct L{
				P s,t;
				L()=default;
				L(P s=P(),P t=P()):s(s),t(t){}
				L(const L&a):s(a.s),t(a.t){}
				D length()const{return dis(s,t);}
			};
			bool LeftTest(const P&a,const L&b){return LeftTest(b.s,b.t,a);}
			bool RightTest(const P&a,const L&b){return RightTest(b.s,b.t,a);}
			bool FrontTest(const P&a,const L&b){return FrontTest(b.s,b.t,a);}
			bool BehindTest(const P&a,const L&b){return BehindTest(b.s,b.t,a);}
			bool PointOnLine(const P&a,const L&b){
				return !sgn((a-b.s)*(b.t-b.s));
			}
			bool PointOnSegment(const P&a,const L&b){
				return !sgn((a-b.s)^(b.t-b.s))&&sgn((b.s-a)*(b.t-a))<=0;
			}
			bool TwoSide(const P&a,const P&b,const L&c){
				return sgn((a-c.s)^(c.t-c.s))*sgn((b-c.s)^(c.t-c.s))<0;
			}
			bool SegmentIntersectJudge(const L&a,const L&b){
				if(PointOnSegment(b.s,a)||PointOnSegment(b.t,a))return 1;
				if(PointOnSegment(a.s,b)||PointOnSegment(a.t,b))return 1;
				return TwoSide(a.s,a.t,b)&&TwoSide(b.s,b.t,a);
			}
			bool LineParallelJudge(const L&a,const L&b){
				return sgn(det(a.t-a.s,b.t-b.s))==0;
			}
			P LineIntersect(const L&a,const L&b){
				if(LineParallelJudge(a,b)){cerr<<"平行线段不相交"<<endl;return P(0,0);}
				D s1=(a.t-a.s)^(b.s-a.s),s2=(a.t-a.s)^(b.t-a.s);
				return (b.s*s2-b.t*s1)/(s2-s1);
			}
			D PointToLine(const P&a,const L&b){
				return fabs((b.t-b.s)^(a-b.s))/dis(b.s,b.t);
			}
			P ProjectToLine(const P&a,const L&b){
				return b.s+(b.t-b.s)*((a-b.s)*(b.t-b.s)/(b.t-b.s).norm2());
			}
			P SymmetryPointToLine(const P&a,const L&b){
				return ProjectToLine(a,b)*2-a;
			}
			D PointToSegment(const P&a,const L&b){
				if(sgn(dot(b.s-a,b.t-b.s)*dot(b.t-a,b.t-b.s))<=0)return PointToLine(a,b);
				return min(dis(a,b.s),dis(a,b.t));
			}
			D AngleCos(const L&a,const L&b){
				return dot(a.t-a.s,b.t-b.s)/a.length()/b.length();
			}
			bool InTriangle(const P&a,const P&b,const P&c,const P&s){
				return (LeftTest(a,b,s)&&LeftTest(b,c,s)&&LeftTest(c,a,s))||(LeftTest(b,a,s)&&LeftTest(c,b,s)&&LeftTest(a,c,s));
			}
struct P3{
	D x,y,z;
	P3(D x=0,D y=0,D z=0):x(x),y(y),z(z){}
	void in(){scanf("%lf%lf%lf",&x,&y,&z);}
	void out(){printf("%.7f %.7f %.7f\n",x,y,z);}
	D norm(){return sqrt(x*x+y*y+z*z);}
	D norm2(){return x*x+y*y+z*z;}
	P3 unit(){
		D l=norm();
		return P3(x/l,y/l,z/l);
	}
	P3 rotate(D w){//三维绕轴旋转，不保证正确 
	//大拇指指向x轴正方向时，4指弯曲由y轴正方向指向z轴正方向，大拇指沿着源点到点(x,y,z)的向量，4指弯曲方向旋转w弧度
	//(x,y,z)*A=(x_new,y_new,z_new) 行向量向右乘转移矩阵 
		D s=norm2(),a[3][3];
		a[0][0]=((y*y+z*z)*cos(w)+x*x)/s;
		a[0][1]=x*y*(1-cos(w))/s+z*sin(w)/sqrt(s);
		a[0][2]=x*z*(1-cos(w))/s-y*sin(w)/sqrt(s);
		a[1][0]=x*y*(1-cos(w))/s-z*sin(w)/sqrt(s);
		a[1][1]=((x*x+z*z)*cos(w)+y*y)/s;
		a[1][2]=y*z*(1-cos(w))/s+x*sin(w)/sqrt(s);
		a[2][0]=x*z*(1-cos(w))/s+y*sin(w)/sqrt(s);
		a[2][1]=y*z*(1-cos(w))/s+x*sin(w)/sqrt(s);
		a[2][2]=((x*x+y*y)*cos(w)+z*z)/s;
		return P3(x*a[0][0]+y*a[1][0]+z*a[2][0],x*a[0][1]+y*a[1][1]+z*a[2][1],x*a[0][2]+y*a[1][2]+z*a[2][2]);
	}
};
bool operator==(P3 a,P3 b){return !cmp(a.x,b.x)&&!cmp(a.y,b.y);}
bool operator!=(P3 a,P3 b){return !(a==b);}
bool operator<(P3 a,P3 b){
	if(cmp(a.x,b.x))return cmp(a.x,b.x)<0;
	if(cmp(a.y,b.y))return cmp(a.y,b.y)<0;
	return cmp(a.z,b.z)<0;
}
P3 operator-(P3 a){return P3(-a.x,-a.y,-a.z);}
P3 operator+(P3 a,P3 b){return P3(a.x+b.x,a.y+b.y,a.z+b.z);}
P3 operator-(P3 a,P3 b){return P3(a.x-b.x,a.y-b.y,a.z-b.z);}
P3 operator*(P3 a,D b){return P3(a.x*b,a.y*b,a.z*b);}
P3 operator/(P3 a,D b){return P3(a.x/b,a.y/b,a.z/b);}
P3 cj(P3 a,P3 b){return P3(a.y*b.z-a.z*b.y,a.z*b.x-a.x*b.z,a.x*b.y-a.y*b.x);}//叉积 
D dj(P3 a,P3 b){return a.x*b.x+a.y*b.y+a.z*b.z;}//点积 
D hhj(P3 a,P3 b,P3 c){return dj(a,cj(b,c));}//混合积，混合积/6即为三个向量构成四面体的体积 
D dis(P3 a,P3 b){return (a-b).norm();}//距离 
D area(P3 a,P3 b,P3 c){return cj(b-a,c-a).norm()*.5;}//空间三角形面积 
struct L3{
	P3 s,t;
	L3(P3 s=P3(),P3 t=P3()):s(s),t(t){}
	void in(){s.in();t.in();}
	D length()const{return dis(s,t);}
};
bool threepoint_on_line(P3 a,P3 b,P3 c){//判断三点共线
	return !sgn(cj(a-b,b-c).norm());
}
bool point_on_line(P3 a,L3 b){//点是否在直线上
	return !sgn(cj(a-b.s,b.t-b.s).norm());
}
bool point_on_segment(P3 a,L3 b){//点是否在线段上
	return !sgn(cj(a-b.s,b.t-b.s).norm())&&sgn(dj(b.s-a,b.t-a))<=0;
}
bool two_side(P3 a,P3 b,L3 c){//两点是否再直线两边
	return sgn(dj(cj(a-c.s,c.t-c.s),cj(b-c.s,c.t-c.s)))<0;
}
bool segment_intersect_judge(L3 a,L3 b){//判断两线段是否相交
	if(point_on_segment(b.s,a)||point_on_segment(b.t,a))return 1;
	if(point_on_segment(a.s,b)||point_on_segment(a.t,b))return 1;
	return two_side(a.s,a.t,b)&&two_side(b.s,b.t,a);
}
P3 line_intersect(L3 a,L3 b){//两直线交点，必须保证共面且不平行 
	P3 p=a.s;
	D t=((a.s.x-b.s.x)*(b.s.y-b.t.y)-(a.s.y-b.s.y)*(b.s.x-b.t.x))/(a.s.x-a.t.x)*(b.s.y-b.t.y)-(a.s.y-a.t.y)*(b.s.x-b.t.x);
	return a.s+(a.t-a.s)*t;
}
D point_to_line(P3 a,L3 b){//点到直线距离
	return cj(b.t-b.s,a-b.s).norm()/dis(b.s,b.t);
}
P3 project_to_line(P3 a,L3 b){//点在直线上投影
	return b.s+(b.t-b.s)*(dj(a-b.s,b.t-b.s)/(b.t-b.s).norm2());
}
P3 duichen(P3 a,L3 b){//点A关于直线B对称点
	P3 c=project_to_line(a,b);
	return c*2-a;
}
D point_to_segment(P3 a,L3 b){//点到线段距离
	if(sgn(dj(b.s-a,b.t-b.s)*dj(b.t-a,b.t-b.s))<=0)return point_to_line(a,b);
	return min(dis(a,b.s),dis(a,b.t));
}
D line_angle_cos(L3 a,L3 b){//两直线夹角的cos 
	return dj(a.t-a.s,b.t-b.s)/a.length()/b.length();
}
struct S3{//可以表示一个平面或者空间里一个三角形 
	P3 a,b,c;
	S3(P3 a=P3(),P3 b=P3(),P3 c=P3()):a(a),b(b),c(c){}
	void in(){a.in();b.in();c.in();}
	P3 base(){return cj(a-b,b-c);}//法向量
};
bool point_on_plane(P3 a,S3 b){//判断点是否在平面上 
	return !sgn(dj(b.base(),a-b.a));
}
bool two_side(P3 a,P3 b,S3 c){//判断两点是否在平面异侧
	return sgn(dj(c.base(),a-c.a)*dj(c.base(),b-c.a))<0;
}
bool plane_parallel(S3 a,S3 b){//判断两平面是否平行
	return !sgn(cj(a.base(),b.base()).norm());
}
bool line_plane_parallel(L3 a,S3 b){//判断直线与平面是否平行
	return !sgn(dj(a.t-a.s,b.base())); 
}
bool plane_vertical(S3 a,S3 b){//判断两平面是否垂直
	return !sgn(dj(a.base(),b.base())); 
}
bool line_plane_vertical(L3 a,S3 b){//判断直线与平面是否垂直
	return !sgn(cj(a.t-a.s,b.base()).norm()); 
}
P3 line_plane_intersect(L3 a,S3 b){//直线与平面交点 
	P3 p=b.base();
	D t=dj(p,b.a-a.s)/dj(p,a.t-a.s);
	return a.s+(a.t-a.s)*t;
}
L3 plane_intersect(S3 a,S3 b){//两平面交线，要保证不平行
	return L3(line_plane_intersect(line_plane_parallel(L3(a.a,a.b),b)?L3(a.b,a.c):L3(a.a,a.b),b),
	line_plane_intersect(line_plane_parallel(L3(a.c,a.a),b)?L3(a.b,a.c):L3(a.c,a.a),b));
}
D point_to_plane(P3 a,S3 b){//点到平面距离
	return fabs(dj(b.base(),a-b.a)/b.base().norm()); 
}
D plane_angle_cos(S3 a,S3 b){//面面角 
	P3 A=a.base(),B=b.base();
	return dj(A,B)/A.norm()/B.norm();
}
D line_plane_angle_sin(L3 a,S3 b){//线面角 
	P3 A=a.t-a.s,B=b.base(); 
	A.out();B.out();
	printf("%.8f\n",dj(A,B));
	return dj(A,B)/A.norm()/B.norm();
}
D volume4(P3 a,P3 b,P3 c,P3 d){//已知四点，利用混合积 
	return hhj(b-a,c-a,d-a)/6;
}
D volume4(D l,D n,D a,D m,D b,D c){//已知六边长求体积 
	D x,y;
	l*=l;n*=n;a*=a;m*=m;b*=b;c*=c;
	x=4*a*b*c-a*(b+c-m)*(b+c-m)-b*(c+a-n)*(c+a-n);
	y=c*(a+b-l)*(a+b-l)-(a+b-l)*(b+c-m)*(c+a-n);
	return (sqrt(x-y)/12);
}
P3 neixin(P3 a,P3 b,P3 c,P3 d){//四面体内心 
	D sa=area(b,c,d),sb=area(a,c,d),sc=area(a,b,d),sd=area(a,b,c);
	return P3(sa*a.x+sb*b.x+sc*c.x+sd*d.x,sa*a.y+sb*b.y+sc*c.y+sd*d.y,sa*a.z+sb*b.z+sc*c.z+sd*d.z)/(sa+sb+sc+sd);
}
bool in_line(P3 a,P3 b,P3 c){
	if(point_on_line(a,L3(b,c)))return true;
	return false;
}
struct PP{
	D x,y,z;
};
bool operator<(PP a,PP b){
	return a.x<b.x;
}
P _p2[W],_p[W];
map<pair<int,int>,int>mp;
int num,id,flag1[N][M],flag2[N][M];
int l[W],r[W],h[W];
double X[16666666],Y[16666666];
P3 e[N][M],f[16666666];
PP pt[4666666];
bool ok[W];
int n,m;
vector<pair<int,int> >V[16666666]; 
vector<P>point_set;
int mx1,mx2;
int best_xld,best_yld,best_xlu,best_ylu,best_xrd,best_yrd,best_xru,best_yru;
vector<tuple<int,int,int,int,int,int,int,int,int> > ANS;
double maxv;
double getR(){
	int x=rand()%32768,y=rand()%32768;
	return 1.0*(x*32768+y)/32768/32768;
}
void update(int epoch,int ld,int lu,int rd,int ru){
	int xld=V[epoch][ld].X,yld=V[epoch][ld].Y;
	int xlu=V[epoch][lu].X,ylu=V[epoch][lu].Y;
	int xrd=V[epoch][rd].X,yrd=V[epoch][rd].Y;
	int xru=V[epoch][ru].X,yru=V[epoch][ru].Y;
	//printf("(%d,%d) (%d,%d) (%d,%d) (%d,%d)\n",xld,yld,xlu,ylu,xrd,yrd,xru,yru);
	P pld=P(xld,yld),plu=P(xlu,ylu),prd=P(xrd,yrd),pru=P(xru,yru);
	if(!SegmentIntersectJudge(L(pld,pru),L(plu,prd)))return;
	//printf("%d\n",abs((ylu-yld)*(xrd-xld)-(yrd-yld)*(xlu-xld))+abs((ylu-yru)*(xrd-xru)-(yrd-yru)*(xlu-xru)));
	//printf("%d\n",maxv);
	//printf("%d %d   %d %d   %d %d    %d %d\n",best_xld,best_yld,best_xlu,best_ylu,best_xrd,best_yrd,best_xru,best_yru);
	int acc=0,wra=0;
	double score=
	min(2*min(abs((ylu-yld)*(xrd-xld)-(yrd-yld)*(xlu-xld)),abs((ylu-yru)*(xrd-xru)-(yrd-yru)*(xlu-xru)))
	-max(abs((ylu-yld)*(xrd-xld)-(yrd-yld)*(xlu-xld)),abs((ylu-yru)*(xrd-xru)-(yrd-yru)*(xlu-xru))),
	2*min(abs((yld-ylu)*(xru-xlu)-(yru-ylu)*(xld-xlu)),abs((yld-yrd)*(xru-xrd)-(xld-xrd)*(yru-yrd)))
	-max(abs((yld-ylu)*(xru-xlu)-(yru-ylu)*(xld-xlu)),abs((yld-yrd)*(xru-xrd)-(xld-xrd)*(yru-yrd))));
	if(score<maxv)return;
	for(int i=min(min(xld,xlu),min(xrd,xru));i<=max(max(xld,xlu),max(xrd,xru));i++)
			for(int j=min(min(yld,ylu),min(yrd,yru));j<=max(max(yld,ylu),max(yrd,yru));j++){
				P o=P(i,j);
				if(InTriangle(pld,plu,prd,o)||InTriangle(plu,prd,pru,o)){
					int x=flag2[i][j]*(mx1+1)+flag1[i][j];
					if(x==epoch)acc++;else wra++;
				}
			}
	if(acc+wra==0)return;
	double rate=1.0*acc/(acc+wra);
	score=score*rate*rate*rate;
	printf("%.8f %.8f\n",rate,score);
	if(score>maxv){
		maxv=score;
		best_xld=xld;
		best_yld=yld;
		best_xlu=xlu;
		best_ylu=ylu;
		best_xrd=xrd;
		best_yrd=yrd;
		best_xru=xru;
		best_yru=yru;
		
	}
}
int RZ(){
	return rand()%32768*32768+rand();
}
int main(int argc, char* argv[]){
	srand(time(0));
	std::string img_dir = argv[1];
	std::cout << img_dir << '\n';
	freopen((img_dir + "/out.txt").c_str(),"r",stdin);
	scanf("%d%d",&n,&m);
	printf("--%d %d\n",n,m);
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++){
			scanf("%d",&flag1[i][j]);
			mx1=max(mx1,flag1[i][j]);
			//if(flag[i][j])V.PB(MP(i,j));
		}
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++){
			scanf("%d",&flag2[i][j]);
			if(flag1[i][j]||flag2[i][j]){
				V[flag2[i][j]*(mx1+1)+flag1[i][j]].PB(MP(i,j));
				mx2=max(flag2[i][j],mx2);
			}
		}
    printf("--%d %d\n",mx1,mx2);
	/*for(int i=1;i<=n/100;i++)
		for(int j=1;j<=m/100;j++){
			printf("(%d,%d)%c",flag1[i*100][j*100],flag2[i*100][j*100],j==m/100?'\n':' ');
		}*/
	//printf("--%d\n",(int)V.size());
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)
			scanf("%lf",&e[i][j].x);
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)
			scanf("%lf",&e[i][j].y);
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)
			scanf("%lf",&e[i][j].z);
	for(int epo=0;epo<=mx2*(mx1+1)+mx1;epo++){
		num=(int)V[epo].size();
		printf("--%d\n",num);
		if(num<=200)continue;
		best_xld=best_yld=best_xlu=best_ylu=best_xrd=best_yrd=best_xru=best_yru=maxv=0;
		for(int i=0;i<num;i++)
			f[i]=e[V[epo][i].X][V[epo][i].Y];
		double x_1=0,y_1=0,z_1=0,x_2=0,y_2=0,z_2=0,x_3=0,y_3=0,z_3=0;
		for(int i=0;i<100;i++){
			int w=RZ()%num;
			x_1+=f[w].x;
			y_1+=f[w].y;
			z_1+=f[w].z;
		}
		for(int i=0;i<100;i++){
			int w=RZ()%num;
			x_2+=f[w].x;
			y_2+=f[w].y;
			z_2+=f[w].z;
		}
		for(int i=0;i<100;i++){
			int w=RZ()%num;
			x_3+=f[w].x;
			y_3+=f[w].y;
			z_3+=f[w].z;
		}
		x_1/=100;y_1/=100;z_1/=100;
		x_2/=100;y_2/=100;z_2/=100;
		x_3/=100;y_3/=100;z_3/=100;
		P3 p1=P3(x_1,y_1,z_1),p2=P3(x_2,y_2,z_2),p3=P3(x_3,y_3,z_3);
		S3 pingmian=S3(p1,p2,p3);
		P3 u=p2-p1;
		P3 v=p3-p1;
		P3 w=pingmian.base();
		S3 pingmian2=S3(p1,p2,p1+w);
		P3 ux=u;
		P3 uy=pingmian2.base();
		uy=uy*(ux.norm()/uy.norm());
		for(int i=0;i<num;i++){
			D __x=dj(f[i]-p1,ux);
			D __y=dj(f[i]-p1,uy);
			_p2[i]=P(__x,__y);
		}
		for(int angle_time=0;angle_time<1000;angle_time++){
			//double seed=getR();
			double angle=pi*angle_time/1000;
			D minx=1e18,miny=1e18,maxx=-1e18,maxy=-1e18;
			for(int i=0;i<num;i++){
				_p[i]=_p2[i].rotate(angle);
				D x=_p[i].x;
				D y=_p[i].y;
				X[i]=x;Y[i]=y;
				minx=min(minx,x);
				miny=min(miny,y);
				maxx=max(maxx,x);
				maxy=max(maxy,y);
			}
			double unit_length_x=(maxx-minx)/sqrt(num);
			double unit_length_y=(maxy-miny)/sqrt(num);
			int max_n=(int)((maxx-minx)/unit_length_x)+1;
			int max_m=(int)((maxy-miny)/unit_length_y)+1;
			for(int i=0;i<=max_n*max_m;i++)ok[i]=0;
			for(int i=0;i<=max_n;i++)for(int j=0;j<=max_m;j++)sz[i][j]=0,to[i][j]=-1;
			for(int i=0;i<num;i++){
				int pos_x=(int)((X[i]-minx)/unit_length_x)+1;
				int pos_y=(int)((Y[i]-miny)/unit_length_y)+1;
				sz[pos_x][pos_y]++;
				if(to[pos_x][pos_y]==-1){
					to[pos_x][pos_y]=i;
				}else{
					if(1ll*(rand()%32768)*sz[pos_x][pos_y]<=32768)to[pos_x][pos_y]=i;
				}
				
				ok[pos_x*max_m+pos_y-max_m]=1;
			}
			for(int i=1;i<=max_m;i++)l[i]=0,r[i]=max_m,h[i]=0; 
			int ans=0,lx,rx,ly,ry;
			for(int i=1;i<=max_n;i++){
				int tmp=1;
				for(int j=1;j<=max_m;j++){
					if(ok[i*max_m+j-max_m]){
						h[j]++;
						l[j]=max(l[j],tmp);
					}else{
						h[j]=0;
						tmp=j+1;
						l[j]=1;
					}
				}
				tmp=max_m;
				for(int j=max_m;j;j--){
					if(ok[i*max_m+j-max_m]){
						r[j]=min(r[j],tmp);
					}else{
						tmp=j-1;
						r[j]=max_m;
					}
					if(h[j]&&r[j]>=l[j]){
						lx=i-h[j]+1;
						rx=i;
						ly=l[j];
						ry=r[j];
						int id_ld=to[lx][ly];
						int id_lu=to[lx][ry];
						int id_rd=to[rx][ly];
						int id_ru=to[rx][ry];
						if(id_ld==-1||id_lu==-1||id_rd==-1||id_ru==-1)continue;
						/*P _ld=P(minx+unit_length_x*(lx-1.0),miny+unit_length_y*(ly-1.0));
						P _lu=P(minx+unit_length_x*(lx-1.0),miny+unit_length_y*(ry-1.0));
						P _rd=P(minx+unit_length_x*(rx-1.0),miny+unit_length_y*(ly-1.0));
						P _ru=P(minx+unit_length_x*(rx-1.0),miny+unit_length_y*(ry-1.0));
						double min_ld=1e18,min_lu=1e18,min_rd=1e18,min_ru=1e18;
						int id_ld,id_lu,id_rd,id_ru;
						for(int l=0;l<num;l++){
							if(dis(_p[l],_ld)<min_ld)min_ld=dis(_p[l],_ld),id_ld=l;
							if(dis(_p[l],_lu)<min_lu)min_lu=dis(_p[l],_lu),id_lu=l;
							if(dis(_p[l],_rd)<min_rd)min_rd=dis(_p[l],_rd),id_rd=l;
							if(dis(_p[l],_ru)<min_ru)min_ru=dis(_p[l],_ru),id_ru=l;
						}*/
						//printf("UP %d %d %d %d\n",id_ld,id_lu,id_rd,id_ru);
						update(epo,id_ld,id_lu,id_rd,id_ru);
					}
					/*if((r[j]-l[j]+1)*h[j]>ans){
						ans=(r[j]-l[j]+1)*h[j];
						lx=i-h[j]+1;
						rx=i;
						ly=l[j];
						ry=r[j];
					}*/
				}
			}
			
			}
		ANS.PB(make_tuple(maxv,best_xld,best_yld,best_xlu,best_ylu,best_xrd,best_yrd,best_xru,best_yru));
	}
	sort(ANS.begin(),ANS.end());
	freopen("process.txt","w",stdout);
	for(int i=0;i<min(10,(int)ANS.size());i++){
		tuple<int,int,int,int,int,int,int,int,int>o=ANS[(int)ANS.size()-i-1];
		printf("%d %d %d %d %d %d %d %d\n",get<1>(o),get<2>(o),get<3>(o),get<4>(o),get<5>(o),get<6>(o),get<7>(o),get<8>(o));
	}
}
