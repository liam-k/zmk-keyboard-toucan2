#include <zephyr/kernel.h>
#include <drivers/behavior.h>
#include <stdio.h>
#include <string.h>

#include "layer_arc.h"
#include "../assets/custom_fonts.h"
#include <zmk/physical_layouts.h>
#include <zmk/keymap.h>
#include <zmk/matrix.h>

#define PRECISION_LAYER_ID 5
#define SCROLL_LAYER_ID 6
#define MODE_ICON_X 8
#define MODE_ICON_Y 117

static void draw_mode_pixel(lv_obj_t *canvas, int x, int y, int width, int height) {
    lv_draw_rect_dsc_t dsc;
    init_rect_dsc(&dsc, LVGL_FOREGROUND);
    dsc.border_width = 0;
    dsc.radius = 0;
    lv_canvas_draw_rect(canvas, x, y, width, height, &dsc);
}

static void draw_precision_icon(lv_obj_t *canvas) {
    draw_mode_pixel(canvas, MODE_ICON_X + 6, MODE_ICON_Y, 2, 4);
    draw_mode_pixel(canvas, MODE_ICON_X + 6, MODE_ICON_Y + 10, 2, 4);
    draw_mode_pixel(canvas, MODE_ICON_X, MODE_ICON_Y + 6, 4, 2);
    draw_mode_pixel(canvas, MODE_ICON_X + 10, MODE_ICON_Y + 6, 4, 2);
    draw_mode_pixel(canvas, MODE_ICON_X + 5, MODE_ICON_Y + 5, 4, 4);
}

static void draw_scroll_icon(lv_obj_t *canvas) {
    draw_mode_pixel(canvas, MODE_ICON_X + 6, MODE_ICON_Y, 2, 14);
    draw_mode_pixel(canvas, MODE_ICON_X + 4, MODE_ICON_Y + 2, 2, 2);
    draw_mode_pixel(canvas, MODE_ICON_X + 8, MODE_ICON_Y + 2, 2, 2);
    draw_mode_pixel(canvas, MODE_ICON_X + 4, MODE_ICON_Y + 10, 2, 2);
    draw_mode_pixel(canvas, MODE_ICON_X + 8, MODE_ICON_Y + 10, 2, 2);
}

static zmk_keymap_layer_index_t highest_standard_layer_active(void) {
    for (int index = ZMK_KEYMAP_LAYERS_LEN - 1; index >= 0; index--) {
        zmk_keymap_layer_id_t layer_id = zmk_keymap_layer_index_to_id(index);

        if (layer_id == PRECISION_LAYER_ID || layer_id == SCROLL_LAYER_ID) {
            continue;
        }

        if (zmk_keymap_layer_active(layer_id)) {
            return index;
        }
    }

    return 0;
}

void draw_layer_status(lv_obj_t *canvas, const struct status_state *state) {
    bool precision_active = zmk_keymap_layer_active(PRECISION_LAYER_ID);
    bool scroll_active = zmk_keymap_layer_active(SCROLL_LAYER_ID);
    zmk_keymap_layer_index_t layer_index = state->layer_index;

    if (precision_active || scroll_active) {
        layer_index = highest_standard_layer_active();
    }

    lv_draw_label_dsc_t label_dsc;
    init_label_dsc(&label_dsc, LVGL_FOREGROUND, &quinquefive_18, LV_TEXT_ALIGN_RIGHT);

    char fallback_layer_name[16];
    const char *layer_name = zmk_keymap_layer_name(zmk_keymap_layer_index_to_id(layer_index));

    if (layer_name == NULL || layer_name[0] == '\0') {
        sprintf(fallback_layer_name, "L#%" PRIu8, layer_index);
        layer_name = fallback_layer_name;
    }

    lv_canvas_draw_text(canvas, -23, 115, SCREEN_WIDTH, &label_dsc, layer_name);

    if (scroll_active) {
        draw_scroll_icon(canvas);
    } else if (precision_active) {
        draw_precision_icon(canvas);
    }
}
