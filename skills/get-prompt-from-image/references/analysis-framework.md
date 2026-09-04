# General Image Analysis Framework

The following content is for internal analysis only and must not be shown to the user.

## 1. Use Case

Determine whether the image is closer to advertising material, a game key visual, social media content, a commercial product photograph, a portrait, a film still, an illustrated poster, a 3D character key visual, an e-commerce hero image, an architectural or interior showcase, food photography, animal photography, a natural landscape or city scene, a graphic poster or visual design, a typeface or logo design, an abstract graphic, or another use case. The use case determines whether the prompt should emphasize narrative, commercial presentation, human expression, product structure, spatial design, or visual communication.

## 2. Medium

Determine whether the image is photography, realistic 3D, semi-realistic 3D, anime-style illustration, painterly illustration, flat vector, product rendering, UI or graphic design, mixed media, or another type. The final Prompt must make the medium boundary explicit, and the Negative Prompt must exclude easily confused media.

## 3. Subject Type

Identify whether the main subject is a person, product, animal, food, architecture or interior, natural landscape, city scene, vehicle, plant or flower, typeface or logo, IP or collectible character, graphic poster or visual design, abstract graphic, mixed subjects, or another type.

Analyze only the specialized rules relevant to the subject type. Without a person, do not analyze expression, gaze, or limbs; without a product, do not analyze packaging or selling points; without an animal, do not analyze fur or gaze; without text, do not analyze typography.

## 4. Composition

Analyze aspect ratio and orientation, subject position and share of the frame, foreground/middle ground/background and negative space, centered/thirds/symmetrical/diagonal/framing/scattered composition, visual structures such as horizontal, vertical, diagonal, triangular, S-shaped, circular, or radial lines, visual center and eye flow, near/far relationships, and the size, occlusion, repetition, balance, and hierarchy among subjects.

## 5. Camera, Viewpoint, and Perspective

Analyze eye-level, high-angle, low-angle, top-down, or aerial views; close-up, half-body, medium shot, full-body, or long shot; wide-angle presence, natural perspective, or spatial compression; near-large/far-small scaling and converging perspective; foreground occlusion and framing; viewing through glass, a window, a doorway, or leaves; depth of field and focus position; and dynamic viewpoints, tilted cameras, or a sense of motion.

Write a specific focal length, aperture, shutter speed, or camera model only when image evidence or metadata is sufficiently clear; otherwise describe only the visual effect.

## 6. Lighting

Analyze key-light direction; hard, soft, back, side, top, or ambient light; natural, studio, three-point, window, neon, or volumetric light; rim light, reflected light, fill light, localized highlights, and shadow placement; bloom, colored flare, light spots, and reflective highlights; overall color temperature and lighting ratio; and how light shapes volume, material, space, and mood.

## 7. Color

Analyze main, supporting, and accent colors; warm or cool tendency; saturation, value, and contrast; monochrome, complementary, analogous, or warm/cool contrast; and tendencies such as neon, sophisticated gray, pastel, vintage, filmic, or commercial clarity. Explain how color guides the eye, separates the subject, and constructs mood.

## 8. Materials

Analyze the surface qualities of the subject and background, including skin, fur, feathers, scales, claws, cloth, fabric, leather, paper, metal, glass, plastic, resin, PVC, acrylic, ceramic, wood, stone, walls, water, liquids, ice, mist, smoke, plants, petals, leaves, dew, screens, packaging, and food surfaces.

Describe reflectivity, roughness, wetness, transparency or translucency, matte finish, softness, hardness, grain, fabric texture, scratches, wrinkles, oily sheen, frost, and powdery qualities, and identify the most important material memory points.

## 9. Depth of Field, Background, and Spatial Layers

Analyze whether the background is sharp or blurred to different degrees, foreground blur, subject-background separation, bokeh, mist, smoke, gradient shadows, textures, tree shadows, reflections, horizontal or vertical lines, diagonal grids, circular light spots, large color blocks, layered mountains, building silhouettes, city lights, and street perspective lines. Determine whether the background carries narrative information or provides atmospheric support. Explain occlusion, scale, and atmospheric perspective among the foreground, middle ground, and background.

## 10. Content and Mood

Analyze the subject’s appearance, shape, size, color, orientation, and state; the positions of supporting elements, props, environmental objects, and decorations; indoor or outdoor setting, location type, time, season, weather, and environmental state; the subject’s action and the narrative or functional relationship among subject, props, and background; and the overall mood and its concrete visual sources.

## 11. Post-Processing and Image Quality

Analyze grain, noise, glow, soft focus, motion blur, film character, chromatic aberration, sharpening, localized highlights, and lens flare; commercial retouching, cinematic color grading, CG-render post-processing, product retouching, skin correction, and material enhancement; as well as clarity, detail density, overexposure, underexposure, excessive skin smoothing, oversharpening, or low resolution.

When high resolution, high detail, or 8K is used as a generation-quality requirement, avoid presenting it as a judgment about the original image’s actual parameters.

## 12. Visual Anchors

Extract the 3–5 elements that most affect similarity from distinctive composition, subject silhouette/pose/proportion, unusual camera relationships, signature lighting, key materials, background geometry, color relationships, spatial layers, and mood constructed from concrete elements. Prioritize them in the first third of the positive Prompt.
