#include<jni.h>
#include<stdio.h>
#include "TestJNI.h"

JNIEXPORT jint JNICALL Java_TestJNI_add(JNIEnv *env,jobject obj,jint n1,jint n2)
{
	jint res;
	res=n1+n2;
	return res;
}
