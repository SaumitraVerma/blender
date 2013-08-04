/*
 * ***** BEGIN GPL LICENSE BLOCK *****
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 * The Original Code is Copyright (C) 2012 Blender Foundation.
 * All rights reserved.
 *
 * The Original Code is: all of this file.
 *
 * Contributor(s):
 *
 * ***** END GPL LICENSE BLOCK *****
 */

/** \file blender/gpu/intern/gpu_object.h
 *  \ingroup gpu
 */

#ifdef __cplusplus
extern "C" {
#endif

#if 0

typedef struct GPU_object_func
{
	void (*gpu_vertex_pointer)  (int size, int type, int stride, const void *pointer);
	void (*gpu_normal_pointer)  (          int type, int stride, const void *pointer);
	void (*gpu_color_pointer )  (int size, int type, int stride, const void *pointer);
	void (*gpu_texcoord_pointer)(int size, int type, int stride, const void *pointer);


#if !defined(GLEW_ES_ONLY)
	void (*gpu_client_active_texture)(int texture);
#endif
	void (*gpuCleanupAfterDraw)(void);


} GPU_object_func;



extern GPU_object_func gpugameobj;

void GPU_init_object_func(void);

#endif

#ifdef __cplusplus
}
#endif
